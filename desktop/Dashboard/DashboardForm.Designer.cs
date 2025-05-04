namespace PiSync.Dashboard
{
    partial class DashboardForm
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
            panel1 = new Panel();
            lblTitle = new Label();
            panelRooms = new FlowLayoutPanel();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(lblTitle);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 0;
            panel1.MouseDown += panel1_MouseDown;
            panel1.MouseMove += panel1_MouseMove;
            panel1.MouseUp += panel1_MouseUp;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(46, 28);
            lblTitle.Margin = new Padding(5, 0, 5, 0);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(157, 30);
            lblTitle.TabIndex = 1;
            lblTitle.Text = "DASHBOARD";
            // 
            // panelRooms
            // 
            panelRooms.AutoScroll = true;
            panelRooms.Dock = DockStyle.Fill;
            panelRooms.Location = new Point(0, 79);
            panelRooms.Name = "panelRooms";
            panelRooms.Size = new Size(875, 441);
            panelRooms.TabIndex = 1;
            // 
            // DashboardForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panelRooms);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "DashboardForm";
            Text = "DashboardForm";
            FormClosed += DashboardForm_FormClosed;
            Load += DashboardForm_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion
        private Label lblTitle;
        private Panel panel1;
        private FlowLayoutPanel panelRooms;
    }
}