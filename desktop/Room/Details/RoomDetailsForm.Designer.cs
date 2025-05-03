namespace PiSync.Room.Details
{
    partial class RoomDetailsForm
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

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(209, 175);
            label1.Name = "label1";
            label1.Size = new Size(82, 22);
            label1.TabIndex = 0;
            label1.Text = "label1";
            // 
            // RoomDetailsForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(763, 483);
            Controls.Add(label1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 3, 4, 3);
            Name = "RoomDetailsForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "ROOM DETAILS";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
    }
}