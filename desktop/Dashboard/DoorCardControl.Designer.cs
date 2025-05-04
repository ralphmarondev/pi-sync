namespace PiSync.Dashboard
{
    partial class DoorCardControl
    {
        /// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            lblDoorStatus = new Label();
            lblDoorName = new Label();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.Lavender;
            panel1.Controls.Add(lblDoorStatus);
            panel1.Controls.Add(lblDoorName);
            panel1.Location = new Point(0, 0);
            panel1.MaximumSize = new Size(140, 140);
            panel1.MinimumSize = new Size(140, 140);
            panel1.Name = "panel1";
            panel1.Size = new Size(150, 150);
            panel1.TabIndex = 0;
            // 
            // lblDoorStatus
            // 
            lblDoorStatus.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
            lblDoorStatus.AutoSize = true;
            lblDoorStatus.Font = new Font("Courier New", 12F);
            lblDoorStatus.Location = new Point(12, 113);
            lblDoorStatus.Name = "lblDoorStatus";
            lblDoorStatus.Size = new Size(58, 22);
            lblDoorStatus.TabIndex = 1;
            lblDoorStatus.Text = "OPEN";
            // 
            // lblDoorName
            // 
            lblDoorName.AutoSize = true;
            lblDoorName.Font = new Font("Courier New", 16F);
            lblDoorName.Location = new Point(12, 18);
            lblDoorName.Name = "lblDoorName";
            lblDoorName.Size = new Size(61, 30);
            lblDoorName.TabIndex = 0;
            lblDoorName.Text = "A16";
            // 
            // DoorCardControl
            // 
            AutoScaleDimensions = new SizeF(9F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(panel1);
            Font = new Font("Courier New", 9F, FontStyle.Regular, GraphicsUnit.Point, 0);
            MaximumSize = new Size(150, 150);
            MinimumSize = new Size(150, 150);
            Name = "DoorCardControl";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label lblDoorStatus;
        private Label lblDoorName;
    }
}
